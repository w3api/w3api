---
title: Component.addPropertyChangeListener()
permalink: /Java/Component/addPropertyChangeListener/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="addPropertyChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addPropertyChangeListener(PropertyChangeListener listener)
public void addPropertyChangeListener(String propertyName, PropertyChangeListener listener)
~~~

## Parámetros
* **PropertyChangeListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeListener listener" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}

## Clase Padre
[Component](/Java/Component/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
