---
title: CharsetEncoder.CharsetEncoder()
permalink: /Java/CharsetEncoder/CharsetEncoder/
date: 2021-01-11
key: Java.C.CharsetEncoder
category: Java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.constructores valor="CharsetEncoder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CharsetEncoder(Charset cs, float averageBytesPerChar, float maxBytesPerChar)
protected CharsetEncoder(Charset cs, float averageBytesPerChar, float maxBytesPerChar, byte[] replacement)
~~~

## Parámetros
* **float maxBytesPerChar**,  {% include w3api/param_description.html metodo=_dato parametro="float maxBytesPerChar" %}
* **float averageBytesPerChar**,  {% include w3api/param_description.html metodo=_dato parametro="float averageBytesPerChar" %}
* **byte[] replacement**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] replacement" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_dato parametro="Charset cs" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CharsetEncoder](/Java/CharsetEncoder/)

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
