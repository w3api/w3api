---
title: DSAPublicKeySpec.DSAPublicKeySpec()
permalink: Java/DSAPublicKeySpec/DSAPublicKeySpec
date: 2021-01-04
key: JavaJava.D.DSAPublicKeySpec
category: java
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
* **BigInteger p**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger p" %}
* **BigInteger y**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger y" %}
* **BigInteger g**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger g" %}
* **BigInteger q**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger q" %}

## Clase Padre
[DSAPublicKeySpec](/Java/DSAPublicKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DSAPublicKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
