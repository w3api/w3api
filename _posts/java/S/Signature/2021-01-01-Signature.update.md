---
title: Signature.update()
permalink: Java/Signature/update
date: 2021-01-11
key: JavaJava.S.Signature
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Signature.metodos valor="update" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void update(byte b) throws SignatureException
public final void update(byte[] data) throws SignatureException
public final void update(byte[] data, int off, int len) throws SignatureException
public final void update(ByteBuffer data) throws SignatureException
~~~

## Parámetros
* **ByteBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer data" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte b**,  {% include w3api/param_description.html metodo=_dato parametro="byte b" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[SignatureException](/Java/SignatureException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Signature](/Java/Signature/)

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
