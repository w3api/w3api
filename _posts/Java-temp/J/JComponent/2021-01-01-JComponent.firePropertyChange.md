---
title: JComponent.firePropertyChange()
permalink: /Java/JComponent/firePropertyChange/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void firePropertyChange(String propertyName, boolean oldValue, boolean newValue)
public void firePropertyChange(String propertyName, int oldValue, int newValue)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="int oldValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean oldValue" %}

## Clase Padre
[JComponent](/Java/JComponent/)

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
