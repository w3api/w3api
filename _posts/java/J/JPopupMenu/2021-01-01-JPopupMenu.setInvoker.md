---
title: JPopupMenu.setInvoker()
permalink: /Java/JPopupMenu/setInvoker/
date: 2021-01-11
key: Java.J.JPopupMenu
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="setInvoker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, expert=true, description="The invoking component for the popup menu") public void setInvoker(Component invoker)
~~~

## Parámetros
* **Component invoker**,  {% include w3api/param_description.html metodo=_dato parametro="Component invoker" %}

## Clase Padre
[JPopupMenu](/Java/JPopupMenu/)

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
