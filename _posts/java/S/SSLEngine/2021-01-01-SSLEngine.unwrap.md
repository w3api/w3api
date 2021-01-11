---
title: SSLEngine.unwrap()
permalink: Java/SSLEngine/unwrap
date: 2021-01-11
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="unwrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SSLEngineResult unwrap(ByteBuffer src, ByteBuffer dst) throws SSLException
public SSLEngineResult unwrap(ByteBuffer src, ByteBuffer[] dsts) throws SSLException
public abstract SSLEngineResult unwrap(ByteBuffer src, ByteBuffer[] dsts, int offset, int length) throws SSLException
~~~

## Parámetros
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **ByteBuffer[] dsts**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] dsts" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [SSLException](/Java/SSLException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/)

## Clase Padre
[SSLEngine](/Java/SSLEngine/)

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
