---
title: Signature.update()
permalink: Java/Signature/update
date: 2021-01-04
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
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **ByteBuffer data**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer data" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte b**,  {% include w3api/param_description.html metodo=_data parametro="byte b" %}

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
{%- for _ldc in site.data.Java.S.Signature.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
