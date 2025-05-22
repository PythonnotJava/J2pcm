import argparse
import sys

from . import *

_NULL_SAFE_SUPPORTED_MODES = {
    "base",
    "dataclass",
    "property",
    "protocol",
    "typeddict"
}

class NoMetavarHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return super()._format_action_invocation(action)
        else:
            return ', '.join(action.option_strings)

def cli():
    parser = argparse.ArgumentParser(
        description="Cli tool for converting JSON to Python class models. Learn more by running: J2pcm -h",
        formatter_class=NoMetavarHelpFormatter
    )
    parser.add_argument(
        "-m", "--mode",
        type=str,
        required=True,
        help="Model type to generate: base, dataclass, nested, property, protocol, typeddict"
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Path to input JSON file"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Path to output Python file."
    )
    parser.add_argument(
        "-n", "--name",
        type=str,
        required=True,
        help="Generate class name."
    )
    parser.add_argument(
        '-c', '--clsattr',
        action='store_true',
        help="Generate class attributes or instance attributes based on Json."
    )
    parser.add_argument(
        "--null-safe",
        action='store_true',
        help="Enable null-safety."
    )
    parser.add_argument(
        '--info',
        action='store_true',
        help='Show methods on Null-Safety support.'
    )
    parser.add_argument(
        '-e', '--encoding',
        type=str,
        default='u8',
        help="Output files's encoding."
    )
    parser.add_argument(
        '--headers',
        type=str,
        default=None,
        help="Add header content to output file."
    )
    parser.add_argument(
        '--ends',
        type=str,
        default=None,
        help="Add end content to output file."
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.info:
        print("✅ Modes that support --null-safe:")
        for mode in _NULL_SAFE_SUPPORTED_MODES:
            print(f"  - {mode}")
        print("❌ 'nested' does NOT support --null-safe")
        sys.exit(0)

    # 设置非_NULL_SAFE_SUPPORTED_MODES方法不支持空安全
    if args.null_safe and args.mode not in _NULL_SAFE_SUPPORTED_MODES:
        print(f"[ERROR] Mode '{args.mode}' does not support --null-safe")
        sys.exit(1)

    if args.mode == "base":
        generate_base_class(
            fileName=args.input,
            output=args.output,
            clsName=args.name,
            clsAttr=bool(args.clsattr),
            encoding=args.encoding,
            nullSafety=bool(args.null_safe),
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    elif args.mode == "dataclass":
        generate_data_class(
            fileName=args.input,
            output=args.output,
            clsName=args.name,
            encoding=args.encoding,
            nullSafety=bool(args.null_safe),
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    elif args.mode == "property":
        generate_property_class(
            fileName=args.input,
            output=args.output,
            clsName=args.name,
            encoding=args.encoding,
            nullSafety=bool(args.null_safe),
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    elif args.mode == "protocol":
        generate_protocol_class(
            fileName=args.input,
            output=args.output,
            clsName=args.name,
            encoding=args.encoding,
            nullSafety=bool(args.null_safe),
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    elif args.mode ==  "typeddict":
        generate_tyed_dict_class(
            fileName=args.input,
            output=args.output,
            clsName=args.name,
            encoding=args.encoding,
            total=False,
            nullSafety=bool(args.null_safe),
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    elif args.mode ==  "nested":
        generate_nested_parallel_class(
            fileName=args.input,
            output=args.output,
            root_class_name=args.name,
            encoding=args.encoding,
            headers=args.headers,
            ends=args.ends
        )
        sys.exit(0)
    else:
        print("❌ Unknown command parameter.")
        sys.exit(1)

__all__ = ['cli']

if __name__ == '__main__':
    cli()