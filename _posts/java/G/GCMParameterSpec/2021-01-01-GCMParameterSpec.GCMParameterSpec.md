---
title: GCMParameterSpec.GCMParameterSpec()
permalink: Java/GCMParameterSpec/GCMParameterSpec
date: 2021-01-11
key: JavaJava.G.GCMParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GCMParameterSpec.constructores valor="GCMParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GCMParameterSpec(int tLen, byte[] src)
public GCMParameterSpec(int tLen, byte[] src, int offset, int len)
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] src" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int tLen**,  {% include w3api/param_description.html metodo=_dato parametro="int tLen" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GCMParameterSpec](/Java/GCMParameterSpec/)

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
