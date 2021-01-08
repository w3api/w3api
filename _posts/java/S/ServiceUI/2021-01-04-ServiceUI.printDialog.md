---
title: ServiceUI.printDialog()
permalink: Java/ServiceUI/printDialog
date: 2021-01-04
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
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **PrintService[] services**,  {% include w3api/param_description.html metodo=_data parametro="PrintService[] services" %}
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="PrintRequestAttributeSet attributes" %}
* **PrintService defaultService**,  {% include w3api/param_description.html metodo=_data parametro="PrintService defaultService" %}
* **GraphicsConfiguration gc**,  {% include w3api/param_description.html metodo=_data parametro="GraphicsConfiguration gc" %}
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_data parametro="DocFlavor flavor" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.S.ServiceUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
