---
title: ECParameterSpec.ECParameterSpec()
permalink: Java/ECParameterSpec/ECParameterSpec
date: 2021-01-04
key: JavaJava.E.ECParameterSpec
category: java
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
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **BigInteger n**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger n" %}
* **ECPoint g**,  {% include w3api/param_description.html metodo=_data parametro="ECPoint g" %}
* **EllipticCurve curve**,  {% include w3api/param_description.html metodo=_data parametro="EllipticCurve curve" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ECParameterSpec](/Java/ECParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ECParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
