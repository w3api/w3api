---
title: DHParameterSpec.DHParameterSpec()
permalink: /Java/DHParameterSpec/DHParameterSpec/
date: 2021-01-11
key: Java.D.DHParameterSpec
category: Java
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
* **BigInteger g**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger g" %}
* **BigInteger p**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger p" %}
* **int l**,  {% include w3api/param_description.html metodo=_dato parametro="int l" %}

## Clase Padre
[DHParameterSpec](/Java/DHParameterSpec/)

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
