---
title: CharsetEncoder.CharsetEncoder()
permalink: Java/CharsetEncoder/CharsetEncoder
date: 2021-01-04
key: JavaJava.C.CharsetEncoder
category: java
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
* **byte[] replacement**,  {% include w3api/param_description.html metodo=_data parametro="byte[] replacement" %}
* **float maxBytesPerChar**,  {% include w3api/param_description.html metodo=_data parametro="float maxBytesPerChar" %}
* **float averageBytesPerChar**,  {% include w3api/param_description.html metodo=_data parametro="float averageBytesPerChar" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_data parametro="Charset cs" %}

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
{%- for _ldc in site.data.Java.C.CharsetEncoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
