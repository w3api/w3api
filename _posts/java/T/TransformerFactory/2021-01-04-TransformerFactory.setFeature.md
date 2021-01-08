---
title: TransformerFactory.setFeature()
permalink: Java/TransformerFactory/setFeature
date: 2021-01-04
key: JavaJava.T.TransformerFactory
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformerFactory.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFeature(String name, boolean value) throws TransformerConfigurationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_data parametro="boolean value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [TransformerConfigurationException](/Java/TransformerConfigurationException/)

## Clase Padre
[TransformerFactory](/Java/TransformerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransformerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
