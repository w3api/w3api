---
title: DigestInputStream.DigestInputStream()
permalink: Java/DigestInputStream/DigestInputStream
date: 2021-01-11
key: JavaJava.D.DigestInputStream
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DigestInputStream.constructores valor="DigestInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DigestInputStream(InputStream stream, MessageDigest digest)
~~~

## Parámetros
* **MessageDigest digest**,  {% include w3api/param_description.html metodo=_dato parametro="MessageDigest digest" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Clase Padre
[DigestInputStream](/Java/DigestInputStream/)

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
