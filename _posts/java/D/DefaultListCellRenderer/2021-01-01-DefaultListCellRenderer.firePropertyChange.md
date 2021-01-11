---
title: DefaultListCellRenderer.firePropertyChange()
permalink: Java/DefaultListCellRenderer/firePropertyChange
date: 2021-01-11
key: JavaJava.D.DefaultListCellRenderer
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultListCellRenderer.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void firePropertyChange(String propertyName, boolean oldValue, boolean newValue)
public void firePropertyChange(String propertyName, byte oldValue, byte newValue)
public void firePropertyChange(String propertyName, char oldValue, char newValue)
public void firePropertyChange(String propertyName, double oldValue, double newValue)
public void firePropertyChange(String propertyName, float oldValue, float newValue)
public void firePropertyChange(String propertyName, int oldValue, int newValue)
public void firePropertyChange(String propertyName, long oldValue, long newValue)
public void firePropertyChange(String propertyName, short oldValue, short newValue)
protected void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **short newValue**,  {% include w3api/param_description.html metodo=_dato parametro="short newValue" %}
* **byte newValue**,  {% include w3api/param_description.html metodo=_dato parametro="byte newValue" %}
* **double newValue**,  {% include w3api/param_description.html metodo=_dato parametro="double newValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **short oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="short oldValue" %}
* **float newValue**,  {% include w3api/param_description.html metodo=_dato parametro="float newValue" %}
* **byte oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="byte oldValue" %}
* **double oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="double oldValue" %}
* **char oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="char oldValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **long newValue**,  {% include w3api/param_description.html metodo=_dato parametro="long newValue" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **long oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="long oldValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **char newValue**,  {% include w3api/param_description.html metodo=_dato parametro="char newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="int oldValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean oldValue" %}
* **float oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="float oldValue" %}

## Clase Padre
[DefaultListCellRenderer](/Java/DefaultListCellRenderer/)

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
