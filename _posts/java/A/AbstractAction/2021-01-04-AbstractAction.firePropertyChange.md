---
title: AbstractAction.firePropertyChange()
permalink: Java/AbstractAction/firePropertyChange
date: 2021-01-04
key: JavaJava.A.AbstractAction
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractAction.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}

## Clase Padre
[AbstractAction](/Java/AbstractAction/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractAction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
