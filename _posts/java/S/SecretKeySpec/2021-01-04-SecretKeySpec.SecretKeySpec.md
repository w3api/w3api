---
title: SecretKeySpec.SecretKeySpec()
permalink: Java/SecretKeySpec/SecretKeySpec
date: 2021-01-04
key: JavaJava.S.SecretKeySpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeySpec.constructores valor="SecretKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SecretKeySpec(byte[] key, int offset, int len, String algorithm)
public SecretKeySpec(byte[] key, String algorithm)
~~~

## Parámetros
* **byte[] key**,  {% include w3api/param_description.html metodo=_data parametro="byte[] key" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SecretKeySpec](/Java/SecretKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecretKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
