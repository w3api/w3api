---
title: ServiceUI.printDialog()
permalink: Java/ServiceUI/printDialog
date: 2021-01-11
key: JavaJava.S.ServiceUI
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceUI.metodos valor="printDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static PrintService printDialog(GraphicsConfiguration gc, int x, int y, PrintService[] services, PrintService defaultService, DocFlavor flavor, PrintRequestAttributeSet attributes) throws HeadlessException
~~~

## Parámetros
* **PrintService defaultService**,  {% include w3api/param_description.html metodo=_dato parametro="PrintService defaultService" %}
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}
* **PrintService[] services**,  {% include w3api/param_description.html metodo=_dato parametro="PrintService[] services" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="PrintRequestAttributeSet attributes" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **GraphicsConfiguration gc**,  {% include w3api/param_description.html metodo=_dato parametro="GraphicsConfiguration gc" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ServiceUI](/Java/ServiceUI/)

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
