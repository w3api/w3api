---
title: DOMConfiguration.setParameter()
permalink: /Java/DOMConfiguration/setParameter/
date: 2021-01-11
key: Java.D.DOMConfiguration
category: Java
tags: ['java se', 'org.w3c.dom', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMConfiguration.metodos valor="setParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setParameter(String name, Object value) throws DOMException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[DOMConfiguration](/Java/DOMConfiguration/)

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
