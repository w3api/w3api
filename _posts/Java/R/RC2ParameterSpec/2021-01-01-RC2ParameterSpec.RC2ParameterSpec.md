---
title: RC2ParameterSpec.RC2ParameterSpec()
permalink: /Java/RC2ParameterSpec/RC2ParameterSpec/
date: 2021-01-11
key: Java.R.RC2ParameterSpec
category: Java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RC2ParameterSpec.constructores valor="RC2ParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RC2ParameterSpec(int effectiveKeyBits)
public RC2ParameterSpec(int effectiveKeyBits, byte[] iv)
public RC2ParameterSpec(int effectiveKeyBits, byte[] iv, int offset)
~~~

## Parámetros
* **byte[] iv**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] iv" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int effectiveKeyBits**,  {% include w3api/param_description.html metodo=_dato parametro="int effectiveKeyBits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RC2ParameterSpec](/Java/RC2ParameterSpec/)

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
