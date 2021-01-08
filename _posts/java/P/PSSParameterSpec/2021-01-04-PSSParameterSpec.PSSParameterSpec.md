---
title: PSSParameterSpec.PSSParameterSpec()
permalink: Java/PSSParameterSpec/PSSParameterSpec
date: 2021-01-04
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
* **int trailerField**,  {% include w3api/param_description.html metodo=_data parametro="int trailerField" %}
* **String mdName**,  {% include w3api/param_description.html metodo=_data parametro="String mdName" %}
* **int saltLen**,  {% include w3api/param_description.html metodo=_data parametro="int saltLen" %}
* **AlgorithmParameterSpec mgfSpec**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec mgfSpec" %}
* **String mgfName**,  {% include w3api/param_description.html metodo=_data parametro="String mgfName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PSSParameterSpec](/Java/PSSParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PSSParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
