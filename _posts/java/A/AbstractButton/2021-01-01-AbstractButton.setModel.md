---
title: AbstractButton.setModel()
permalink: /Java/AbstractButton/setModel/
date: 2021-01-11
key: Java.A.AbstractButton
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Model that the Button uses.") public void setModel(ButtonModel newModel)
~~~

## Parámetros
* **ButtonModel newModel**,  {% include w3api/param_description.html metodo=_dato parametro="ButtonModel newModel" %}

## Clase Padre
[AbstractButton](/Java/AbstractButton/)

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
