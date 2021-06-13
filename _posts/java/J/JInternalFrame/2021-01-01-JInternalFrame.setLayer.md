---
title: JInternalFrame.setLayer()
permalink: /Java/JInternalFrame/setLayer/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setLayer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, expert=true, description="Specifies what desktop layer is used.") public void setLayer(int layer)
@BeanProperty(bound=false, expert=true, description="Specifies what desktop layer is used.") public void setLayer(Integer layer)
~~~

## Parámetros
* **Integer layer**,  {% include w3api/param_description.html metodo=_dato parametro="Integer layer" %}
* **int layer**,  {% include w3api/param_description.html metodo=_dato parametro="int layer" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JInternalFrame](/Java/JInternalFrame/)

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
