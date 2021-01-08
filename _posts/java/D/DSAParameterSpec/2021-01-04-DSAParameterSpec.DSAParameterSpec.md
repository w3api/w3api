---
title: DSAParameterSpec.DSAParameterSpec()
permalink: Java/DSAParameterSpec/DSAParameterSpec
date: 2021-01-04
key: JavaJava.D.DSAParameterSpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DSAParameterSpec.constructores valor="DSAParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DSAParameterSpec(BigInteger p, BigInteger q, BigInteger g)
~~~

## Parámetros
* **BigInteger p**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger p" %}
* **BigInteger g**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger g" %}
* **BigInteger q**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger q" %}

## Clase Padre
[DSAParameterSpec](/Java/DSAParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DSAParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
