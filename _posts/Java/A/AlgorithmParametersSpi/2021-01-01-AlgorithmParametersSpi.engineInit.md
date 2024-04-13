---
title: AlgorithmParametersSpi.engineInit()
permalink: /Java/AlgorithmParametersSpi/engineInit/
date: 2021-01-11
key: Java.A.AlgorithmParametersSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParametersSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(byte[] params) throws IOException
protected abstract void engineInit(byte[] params, String format) throws IOException
protected abstract void engineInit(AlgorithmParameterSpec paramSpec) throws InvalidParameterSpecException
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}
* **byte[] params**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] params" %}
* **AlgorithmParameterSpec paramSpec**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec paramSpec" %}

## Excepciones
[InvalidParameterSpecException](/Java/InvalidParameterSpecException/), [IOException](/Java/IOException/)

## Clase Padre
[AlgorithmParametersSpi](/Java/AlgorithmParametersSpi/)

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
