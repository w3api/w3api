---
title: AsynchronousSocketChannel.connect()
permalink: Java/AsynchronousSocketChannel/connect
date: 2021-01-11
key: JavaJava.A.AsynchronousSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousSocketChannel.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Future<Void> connect(SocketAddress remote)
abstract <A> void connect(SocketAddress remote, A attachment, CompletionHandler<Void,? super A> handler)
~~~

## Parámetros
* **CompletionHandler&lt;Void**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<Void" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super A> handler" %}
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress remote" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}

## Excepciones
[UnresolvedAddressException](/Java/UnresolvedAddressException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ConnectionPendingException](/Java/ConnectionPendingException/), [SecurityException](/Java/SecurityException/), [AlreadyConnectedException](/Java/AlreadyConnectedException/)

## Clase Padre
[AsynchronousSocketChannel](/Java/AsynchronousSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
