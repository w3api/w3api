---
title: OAEPParameterSpec.OAEPParameterSpec()
permalink: Java/OAEPParameterSpec/OAEPParameterSpec
date: 2021-01-04
key: JavaJava.O.OAEPParameterSpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OAEPParameterSpec.constructores valor="OAEPParameterSpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OAEPParameterSpec(String mdName, String mgfName, AlgorithmParameterSpec mgfSpec, PSource pSrc)
~~~

## Parámetros
* **AlgorithmParameterSpec mgfSpec**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec mgfSpec" %}
* **String mgfName**,  {% include w3api/param_description.html metodo=_data parametro="String mgfName" %}
* **String mdName**,  {% include w3api/param_description.html metodo=_data parametro="String mdName" %}
* **PSource pSrc**,  {% include w3api/param_description.html metodo=_data parametro="PSource pSrc" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OAEPParameterSpec](/Java/OAEPParameterSpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OAEPParameterSpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
