---
title: JTabbedPane.setDisabledIconAt()
permalink: /Java/JTabbedPane/setDisabledIconAt/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setDisabledIconAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, description="The disabled icon at the specified tab index.") public void setDisabledIconAt(int index, Icon disabledIcon)
~~~

## Parámetros
* **Icon disabledIcon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon disabledIcon" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
