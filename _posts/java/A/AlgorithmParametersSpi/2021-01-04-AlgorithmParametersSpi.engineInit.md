---
title: AlgorithmParametersSpi.engineInit()
permalink: Java/AlgorithmParametersSpi/engineInit
date: 2021-01-04
key: JavaJava.A.AlgorithmParametersSpi
category: java
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
* **AlgorithmParameterSpec paramSpec**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec paramSpec" %}
* **byte[] params**,  {% include w3api/param_description.html metodo=_data parametro="byte[] params" %}
* **String format**,  {% include w3api/param_description.html metodo=_data parametro="String format" %}

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
{%- for _ldc in site.data.Java.A.AlgorithmParametersSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
