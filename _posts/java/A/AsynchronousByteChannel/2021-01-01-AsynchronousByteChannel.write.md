---
title: AsynchronousByteChannel.write()
permalink: Java/AsynchronousByteChannel/write
date: 2021-01-11
key: JavaJava.A.AsynchronousByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousByteChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Future<Integer> write(ByteBuffer src)
<A> void write(ByteBuffer src, A attachment, CompletionHandler<Integer,? super A> handler)
~~~

## Parámetros
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<Integer" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super A> handler" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}

## Excepciones
[WritePendingException](/Java/WritePendingException/)

## Clase Padre
[AsynchronousByteChannel](/Java/AsynchronousByteChannel/)

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
