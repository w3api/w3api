---
title: AlgorithmParametersSpi.engineGetParameterSpec()
permalink: Java/AlgorithmParametersSpi/engineGetParameterSpec
date: 2021-01-10
key: JavaJava.A.AlgorithmParametersSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlgorithmParametersSpi.metodos valor="engineGetParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract <T extends AlgorithmParameterSpec>T engineGetParameterSpec(Class<T> paramSpec)
~~~

## Parámetros
* **Class&lt;T&gt; paramSpec**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> paramSpec" %}

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
