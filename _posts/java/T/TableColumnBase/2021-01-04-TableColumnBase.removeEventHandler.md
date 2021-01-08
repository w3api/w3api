---
title: TableColumnBase.removeEventHandler()
permalink: Java/TableColumnBase/removeEventHandler
date: 2021-01-04
key: JavaJava.T.TableColumnBase
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableColumnBase.metodos valor="removeEventHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<E extends Event>void removeEventHandler(EventType<E> eventType, EventHandler<E> eventHandler)
~~~

## Parámetros
* **EventHandler&lt;E&gt; eventHandler**,  {% include w3api/param_description.html metodo=_data parametro="EventHandler<E> eventHandler" %}
* **EventType&lt;E&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<E> eventType" %}

## Clase Padre
[TableColumnBase](/Java/TableColumnBase/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableColumnBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
