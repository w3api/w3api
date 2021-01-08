---
title: DSAPrivateKeySpec.DSAPrivateKeySpec()
permalink: Java/DSAPrivateKeySpec/DSAPrivateKeySpec
date: 2021-01-04
key: JavaJava.D.DSAPrivateKeySpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DSAPrivateKeySpec.constructores valor="DSAPrivateKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DSAPrivateKeySpec(BigInteger x, BigInteger p, BigInteger q, BigInteger g)
~~~

## Parámetros
* **BigInteger p**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger p" %}
* **BigInteger g**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger g" %}
* **BigInteger x**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger x" %}
* **BigInteger q**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger q" %}

## Clase Padre
[DSAPrivateKeySpec](/Java/DSAPrivateKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DSAPrivateKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
