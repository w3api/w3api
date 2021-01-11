---
title: PSSParameterSpec.PSSParameterSpec()
permalink: Java/PSSParameterSpec/PSSParameterSpec
date: 2021-01-11
key: JavaJava.P.PSSParameterSpec
category: java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PSSParameterSpec.constructores valor="PSSParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PSSParameterSpec(int saltLen)
public PSSParameterSpec(String mdName, String mgfName, AlgorithmParameterSpec mgfSpec, int saltLen, int trailerField)
~~~

## Parámetros
* **String mgfName**,  {% include w3api/param_description.html metodo=_dato parametro="String mgfName" %}
* **int trailerField**,  {% include w3api/param_description.html metodo=_dato parametro="int trailerField" %}
* **AlgorithmParameterSpec mgfSpec**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec mgfSpec" %}
* **String mdName**,  {% include w3api/param_description.html metodo=_dato parametro="String mdName" %}
* **int saltLen**,  {% include w3api/param_description.html metodo=_dato parametro="int saltLen" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PSSParameterSpec](/Java/PSSParameterSpec/)

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
