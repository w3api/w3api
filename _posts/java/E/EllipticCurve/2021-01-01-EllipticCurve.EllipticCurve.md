---
title: EllipticCurve.EllipticCurve()
permalink: Java/EllipticCurve/EllipticCurve
date: 2021-01-11
key: JavaJava.E.EllipticCurve
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EllipticCurve.constructores valor="EllipticCurve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EllipticCurve(ECField field, BigInteger a, BigInteger b)
public EllipticCurve(ECField field, BigInteger a, BigInteger b, byte[] seed)
~~~

## Parámetros
* **byte[] seed**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] seed" %}
* **BigInteger b**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger b" %}
* **ECField field**,  {% include w3api/param_description.html metodo=_dato parametro="ECField field" %}
* **BigInteger a**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger a" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[EllipticCurve](/Java/EllipticCurve/)

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
