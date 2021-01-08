---
title: AsynchronousSocketChannel.connect()
permalink: Java/AsynchronousSocketChannel/connect
date: 2021-01-04
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
* **CompletionHandler&lt;Void**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<Void" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **SocketAddress remote**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress remote" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [ConnectionPendingException](/Java/ConnectionPendingException/), [AlreadyConnectedException](/Java/AlreadyConnectedException/), [UnresolvedAddressException](/Java/UnresolvedAddressException/)

## Clase Padre
[AsynchronousSocketChannel](/Java/AsynchronousSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
