---
title: IvParameterSpec.IvParameterSpec()
permalink: Java/IvParameterSpec/IvParameterSpec
date: 2021-01-04
key: JavaJava.I.IvParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IvParameterSpec.constructores valor="IvParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IvParameterSpec(byte[] iv)
public IvParameterSpec(byte[] iv, int offset, int len)
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **byte[] iv**,  {% include w3api/param_description.html metodo=_data parametro="byte[] iv" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IvParameterSpec](/Java/IvParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IvParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
