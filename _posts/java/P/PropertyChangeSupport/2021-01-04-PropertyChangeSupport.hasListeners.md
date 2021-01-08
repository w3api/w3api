---
title: PropertyChangeSupport.hasListeners()
permalink: Java/PropertyChangeSupport/hasListeners
date: 2021-01-04
key: JavaJava.P.PropertyChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeSupport.metodos valor="hasListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean hasListeners(String propertyName)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}

## Clase Padre
[PropertyChangeSupport](/Java/PropertyChangeSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
