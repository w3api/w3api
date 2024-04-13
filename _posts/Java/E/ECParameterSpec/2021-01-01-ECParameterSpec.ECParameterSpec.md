---
title: ECParameterSpec.ECParameterSpec()
permalink: /Java/ECParameterSpec/ECParameterSpec/
date: 2021-01-11
key: Java.E.ECParameterSpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ECParameterSpec.constructores valor="ECParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ECParameterSpec(EllipticCurve curve, ECPoint g, BigInteger n, int h)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **BigInteger n**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger n" %}
* **EllipticCurve curve**,  {% include w3api/param_description.html metodo=_dato parametro="EllipticCurve curve" %}
* **ECPoint g**,  {% include w3api/param_description.html metodo=_dato parametro="ECPoint g" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ECParameterSpec](/Java/ECParameterSpec/)

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
