---
title: WebEngine.setOnStatusChanged()
permalink: /Java/WebEngine/setOnStatusChanged/
date: 2021-01-11
key: Java.W.WebEngine
category: Java
tags: ['java se', 'javafx.scene.web', 'javafx.web', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebEngine.metodos valor="setOnStatusChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setOnStatusChanged(EventHandler<WebEvent<String>> handler)
~~~

## Parámetros
* **EventHandler&lt;WebEvent&lt;String&gt;&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="EventHandler<WebEvent<String>> handler" %}

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
