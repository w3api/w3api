---
title: GCMParameterSpec.GCMParameterSpec()
permalink: Java/GCMParameterSpec/GCMParameterSpec
date: 2021-01-04
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
* **int tLen**,  {% include w3api/param_description.html metodo=_data parametro="int tLen" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_data parametro="byte[] src" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.G.GCMParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
