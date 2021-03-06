---
title: XPathFactory.setFeature()
permalink: /Java/XPathFactory/setFeature/
date: 2021-01-11
key: Java.X.XPathFactory
category: Java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathFactory.metodos valor="setFeature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setFeature(String name, boolean value) throws XPathFactoryConfigurationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[XPathFactoryConfigurationException](/Java/XPathFactoryConfigurationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XPathFactory](/Java/XPathFactory/)

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
