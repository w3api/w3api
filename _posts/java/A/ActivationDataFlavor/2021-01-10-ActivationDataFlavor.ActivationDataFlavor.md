---
title: ActivationDataFlavor.ActivationDataFlavor()
permalink: Java/ActivationDataFlavor/ActivationDataFlavor
date: 2021-01-10
key: JavaJava.A.ActivationDataFlavor
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationDataFlavor.constructores valor="ActivationDataFlavor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ActivationDataFlavor(Class representationClass, String humanPresentableName)
public ActivationDataFlavor(Class representationClass, String mimeType, String humanPresentableName)
public ActivationDataFlavor(String mimeType, String humanPresentableName)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **Class representationClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class representationClass" %}
* **String humanPresentableName**,  {% include w3api/param_description.html metodo=_dato parametro="String humanPresentableName" %}

## Clase Padre
[ActivationDataFlavor](/Java/ActivationDataFlavor/)

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
