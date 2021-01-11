---
title: DefaultTableCellRenderer.firePropertyChange()
permalink: Java/DefaultTableCellRenderer/firePropertyChange
date: 2021-01-11
key: JavaJava.D.DefaultTableCellRenderer
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableCellRenderer.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void firePropertyChange(String propertyName, boolean oldValue, boolean newValue)
protected void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean oldValue" %}

## Clase Padre
[DefaultTableCellRenderer](/Java/DefaultTableCellRenderer/)

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
