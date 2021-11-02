---
title: socketserver.BaseServer
permalink: /Python/socketserver/BaseServer/
date: 2021-01-01
key: Python.S.socketserver.BaseServer
category: python
tags: ['clase python', 'socketserver']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.S.socketserver.BaseServer.metodos valor="socketserver/BaseServer" %}

## Descripción
{{site.data.Python.S.socketserver.BaseServer.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.socketserver.BaseServer.sintaxis }}~~~

## Constructores
* [BaseServer](/Python/socketserver/BaseServer/BaseServer/)

## Métodos
* [fileno](/Python/socketserver/BaseServer/fileno/)
* [finish_request](/Python/socketserver/BaseServer/finish_request/)
* [get_request](/Python/socketserver/BaseServer/get_request/)
* [handle_error](/Python/socketserver/BaseServer/handle_error/)
* [handle_request](/Python/socketserver/BaseServer/handle_request/)
* [handle_timeout](/Python/socketserver/BaseServer/handle_timeout/)
* [process_request](/Python/socketserver/BaseServer/process_request/)
* [server_activate](/Python/socketserver/BaseServer/server_activate/)
* [server_bind](/Python/socketserver/BaseServer/server_bind/)
* [server_close](/Python/socketserver/BaseServer/server_close/)
* [serve_forever](/Python/socketserver/BaseServer/serve_forever/)
* [service_actions](/Python/socketserver/BaseServer/service_actions/)
* [shutdown](/Python/socketserver/BaseServer/shutdown/)
* [verify_request](/Python/socketserver/BaseServer/verify_request/)

## Atributos
* [address_family](/Python/socketserver/BaseServer/address_family/)
* [allow_reuse_address](/Python/socketserver/BaseServer/allow_reuse_address/)
* [RequestHandlerClass](/Python/socketserver/BaseServer/RequestHandlerClass/)
* [request_queue_size](/Python/socketserver/BaseServer/request_queue_size/)
* [server_address](/Python/socketserver/BaseServer/server_address/)
* [socket](/Python/socketserver/BaseServer/socket/)
* [socket_type](/Python/socketserver/BaseServer/socket_type/)
* [timeout](/Python/socketserver/BaseServer/timeout/)

## Ejemplo
~~~python
{{ site.data.Python.S.socketserver.BaseServer.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.socketserver.BaseServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
