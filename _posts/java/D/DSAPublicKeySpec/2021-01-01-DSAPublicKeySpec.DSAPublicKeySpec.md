---
title: DSAPublicKeySpec.DSAPublicKeySpec()
permalink: /Java/DSAPublicKeySpec/DSAPublicKeySpec/
date: 2021-01-11
key: Java.D.DSAPublicKeySpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DSAPublicKeySpec.constructores valor="DSAPublicKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DSAPublicKeySpec(BigInteger y, BigInteger p, BigInteger q, BigInteger g)
~~~

## Parámetros
* **BigInteger g**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger g" %}
* **BigInteger p**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger p" %}
* **BigInteger y**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger y" %}
* **BigInteger q**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger q" %}

## Clase Padre
[DSAPublicKeySpec](/Java/DSAPublicKeySpec/)

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
