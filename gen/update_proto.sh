cd /Users/chenpeng/cc-server/proto/
python3 -m grpc_tools.protoc --python_out=/Users/chenpeng/yX_Proj/spin_client/gen/proto --grpc_python_out=/Users/chenpeng/yX_Proj/spin_client/gen/gprc_proto -I. *.proto
cd /Users/chenpeng/yX_Proj/spin_client
