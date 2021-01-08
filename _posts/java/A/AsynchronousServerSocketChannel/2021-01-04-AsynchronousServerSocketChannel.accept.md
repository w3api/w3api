---
title: AsynchronousServerSocketChannel.accept()
permalink: Java/AsynchronousServerSocketChannel/accept
date: 2021-01-04
key: JavaJava.A.AsynchronousServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousServerSocketChannel.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Future<AsynchronousSocketChannel> accept()
abstract <A> void accept(A attachment, CompletionHandler<AsynchronousSocketChannel,? super A> handler)
~~~

## Parámetros
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="? super A> handler" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_data parametro="A attachment" %}
* **CompletionHandler&lt;AsynchronousSocketChannel**,  {% include w3api/param_description.html metodo=_data parametro="CompletionHandler<AsynchronousSocketChannel" %}

## Excepciones
[AcceptPendingException](/Java/AcceptPendingException/), [NotYetBoundException](/Java/NotYetBoundException/)

## Clase Padre
[AsynchronousServerSocketChannel](/Java/AsynchronousServerSocketChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousServerSocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
