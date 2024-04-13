---
title: AsynchronousByteChannel.read()
permalink: /Java/AsynchronousByteChannel/read/
date: 2021-01-11
key: Java.A.AsynchronousByteChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousByteChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Future<Integer> read(ByteBuffer dst)
<A> void read(ByteBuffer dst, A attachment, CompletionHandler<Integer,? super A> handler)
~~~

## Parámetros
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **CompletionHandler&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionHandler<Integer" %}
* **? super A&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super A> handler" %}
* **A attachment**,  {% include w3api/param_description.html metodo=_dato parametro="A attachment" %}

## Excepciones
[ReadPendingException](/Java/ReadPendingException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
