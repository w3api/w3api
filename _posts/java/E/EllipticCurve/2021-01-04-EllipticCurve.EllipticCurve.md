---
title: EllipticCurve.EllipticCurve()
permalink: Java/EllipticCurve/EllipticCurve
date: 2021-01-04
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
* **ECField field**,  {% include w3api/param_description.html metodo=_data parametro="ECField field" %}
* **BigInteger b**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger b" %}
* **BigInteger a**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger a" %}
* **byte[] seed**,  {% include w3api/param_description.html metodo=_data parametro="byte[] seed" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EllipticCurve](/Java/EllipticCurve/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EllipticCurve.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
