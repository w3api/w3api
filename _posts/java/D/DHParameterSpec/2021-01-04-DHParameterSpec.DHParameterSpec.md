---
title: DHParameterSpec.DHParameterSpec()
permalink: Java/DHParameterSpec/DHParameterSpec
date: 2021-01-04
key: JavaJava.D.DHParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DHParameterSpec.constructores valor="DHParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DHParameterSpec(BigInteger p, BigInteger g)
public DHParameterSpec(BigInteger p, BigInteger g, int l)
~~~

## Parámetros
* **BigInteger p**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger p" %}
* **int l**,  {% include w3api/param_description.html metodo=_data parametro="int l" %}
* **BigInteger g**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger g" %}

## Clase Padre
[DHParameterSpec](/Java/DHParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DHParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
