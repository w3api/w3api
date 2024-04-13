---
title: WebEngine.setOnResized()
permalink: /Java/WebEngine/setOnResized/
date: 2021-01-11
key: Java.W.WebEngine
category: Java
tags: ['java se', 'javafx.scene.web', 'javafx.web', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebEngine.metodos valor="setOnResized" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setOnResized(EventHandler<WebEvent<Rectangle2D>> handler)
~~~

## Parámetros
* **EventHandler&lt;WebEvent&lt;Rectangle2D&gt;&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="EventHandler<WebEvent<Rectangle2D>> handler" %}

## Clase Padre
[WebEngine](/Java/WebEngine/)

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
